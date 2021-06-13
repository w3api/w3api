---
title: Marshaller.getNode()
permalink: Java/Marshaller/getNode
date: 2021-01-11
key: JavaJava.M.Marshaller
category: Java
tags: ['java se', 'javax.xml.bind', 'java.xml.bind', 'metodo java', 'Java 1.6', 'JAXB Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.M.Marshaller.metodos valor="getNode" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
Node getNode(Object contentTree) throws JAXBException
~~~

## Parámetros
* **Object contentTree**,  {% include w3api/param_description.html metodo=_dato parametro="Object contentTree" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/), [JAXBException](/Java/JAXBException/), [UnsupportedOperationException](/Java/UnsupportedOperationException/)

## Clase Padre
[Marshaller](/Java/Marshaller/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
