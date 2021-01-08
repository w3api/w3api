---
title: Recording.disable()
permalink: Java/Recording/disable
date: 2021-01-04
key: JavaJava.R.Recording
category: java
tags: ['java se', 'jdk.jfr', 'jdk.jfr', 'metodo java', 'Java 9']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.R.Recording.metodos valor="disable" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public EventSettings disable(Class<? extends Event> eventClass)
public EventSettings disable(String name)
~~~

## Parámetros
* **Class&lt;? extends Event&gt; eventClass**,  {% include w3api/param_description.html metodo=_data parametro="Class<? extends Event> eventClass" %}
* **String name**,  {% include w3api/param_description.html metodo=_data parametro="String name" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[Recording](/Java/Recording/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.R.Recording.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
