---
title: LogManager.updateConfiguration()
permalink: /Java/LogManager/updateConfiguration/
date: 2021-01-11
key: Java.L.LogManager
category: Java
tags: ['java se', 'java.util.logging', 'java.logging', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.L.LogManager.metodos valor="updateConfiguration" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void updateConfiguration(InputStream ins, Function<String,BiFunction<String,String,String>> mapper) throws IOException
public void updateConfiguration(Function<String,BiFunction<String,String,String>> mapper) throws IOException
~~~

## Parámetros
* **BiFunction&lt;String**,  {% include w3api/param_description.html metodo=_dato parametro="BiFunction<String" %}
* **InputStream ins**,  {% include w3api/param_description.html metodo=_dato parametro="InputStream ins" %}
* **Function&lt;String**,  {% include w3api/param_description.html metodo=_dato parametro="Function<String" %}
* **String&gt;&gt; mapper**,  {% include w3api/param_description.html metodo=_dato parametro="String>> mapper" %}
* **String**,  {% include w3api/param_description.html metodo=_dato parametro="String" %}

## Excepciones
[SecurityException](/Java/SecurityException/), [IOException](/Java/IOException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[LogManager](/Java/LogManager/)

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
