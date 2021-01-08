---
title: EventTypeInfo.from()
permalink: Java/EventTypeInfo/from
date: 2021-01-04
key: JavaJava.E.EventTypeInfo
category: java
tags: ['java se', 'jdk.management.jfr', 'jdk.management.jfr', 'metodo java', 'Java 9']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.E.EventTypeInfo.metodos valor="from" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static EventTypeInfo from(CompositeData cd)
~~~

## Parámetros
* **CompositeData cd**,  {% include w3api/param_description.html metodo=_data parametro="CompositeData cd" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[EventTypeInfo](/Java/EventTypeInfo/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.E.EventTypeInfo.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
