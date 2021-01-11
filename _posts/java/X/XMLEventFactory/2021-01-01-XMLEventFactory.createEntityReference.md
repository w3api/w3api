---
title: XMLEventFactory.createEntityReference()
permalink: Java/XMLEventFactory/createEntityReference
date: 2021-01-11
key: JavaJava.X.XMLEventFactory
category: java
tags: ['java se', 'javax.xml.stream', 'java.xml', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.X.XMLEventFactory.metodos valor="createEntityReference" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract EntityReference createEntityReference(String name, EntityDeclaration declaration)
~~~

## Parámetros
* **String name**,  {% include w3api/param_description.html metodo=_dato parametro="String name" %}
* **EntityDeclaration declaration**,  {% include w3api/param_description.html metodo=_dato parametro="EntityDeclaration declaration" %}

## Clase Padre
[XMLEventFactory](/Java/XMLEventFactory/)

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
