---
title: JobAttributes.setDestination()
permalink: /Java/JobAttributes/setDestination/
date: 2021-01-11
key: Java.J.JobAttributes
category: Java
tags: ['java se', 'java.awt', 'java.desktop', 'metodo java', 'Java 1.3']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.J.JobAttributes.metodos valor="setDestination" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void setDestination(JobAttributes.DestinationType destination)
~~~

## Parámetros
* **JobAttributes.DestinationType destination**,  {% include w3api/param_description.html metodo=_dato parametro="JobAttributes.DestinationType destination" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[JobAttributes](/Java/JobAttributes/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Artículos
<ul>
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
