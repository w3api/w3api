---
title: Invocable.getInterface()
permalink: Java/Invocable/getInterface
date: 2021-01-11
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
* **Class&lt;T&gt; clasz**,  {% include w3api/param_description.html metodo=_dato parametro="Class<T> clasz" %}
* **Object thiz**,  {% include w3api/param_description.html metodo=_dato parametro="Object thiz" %}

## Clase Padre
[Invocable](/Java/Invocable/)

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
