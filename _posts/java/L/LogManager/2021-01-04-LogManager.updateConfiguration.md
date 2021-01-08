---
title: LogManager.updateConfiguration()
permalink: Java/LogManager/updateConfiguration
date: 2021-01-04
key: JavaJava.L.LogManager
category: java
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
* **String**,  {% include w3api/param_description.html metodo=_data parametro="String" %}
* **BiFunction&lt;String**,  {% include w3api/param_description.html metodo=_data parametro="BiFunction<String" %}
* **String&gt;&gt; mapper**,  {% include w3api/param_description.html metodo=_data parametro="String>> mapper" %}
* **InputStream ins**,  {% include w3api/param_description.html metodo=_data parametro="InputStream ins" %}
* **Function&lt;String**,  {% include w3api/param_description.html metodo=_data parametro="Function<String" %}

## Excepciones
[SecurityException](/Java/SecurityException/), [NullPointerException](/Java/NullPointerException/), [IOException](/Java/IOException/)

## Clase Padre
[LogManager](/Java/LogManager/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.L.LogManager.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
