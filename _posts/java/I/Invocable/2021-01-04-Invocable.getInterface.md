---
title: Invocable.getInterface()
permalink: Java/Invocable/getInterface
date: 2021-01-04
key: JavaJava.I.Invocable
category: java
tags: ['java se', 'javax.script', 'java.scripting', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.I.Invocable.metodos valor="getInterface" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
<T> T getInterface(Class<T> clasz)
<T> T getInterface(Object thiz, Class<T> clasz)
~~~

## Parámetros
* **Object thiz**,  {% include w3api/param_description.html metodo=_data parametro="Object thiz" %}
* **Class&lt;T&gt; clasz**,  {% include w3api/param_description.html metodo=_data parametro="Class<T> clasz" %}

## Clase Padre
[Invocable](/Java/Invocable/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.I.Invocable.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
