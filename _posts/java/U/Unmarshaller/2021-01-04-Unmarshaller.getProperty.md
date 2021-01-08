---
title: Unmarshaller.getProperty()
permalink: Java/Unmarshaller/getProperty
date: 2021-01-04
key: JavaJava.U.Unmarshaller
category: java
tags: ['java se', 'javax.xml.bind', 'java.xml.bind', 'metodo java', 'Java 1.6', 'JAXB Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.U.Unmarshaller.metodos valor="getProperty" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
Object getProperty(String name) throws PropertyException
~~~

## Parámetros
* **String name**,  {% include w3api/param_description.html metodo=_data parametro="String name" %}

## Excepciones
[PropertyException](/Java/PropertyException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[Unmarshaller](/Java/Unmarshaller/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.U.Unmarshaller.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
