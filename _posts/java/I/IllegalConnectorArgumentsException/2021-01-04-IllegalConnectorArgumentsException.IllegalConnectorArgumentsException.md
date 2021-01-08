---
title: IllegalConnectorArgumentsException.IllegalConnectorArgumentsException()
permalink: Java/IllegalConnectorArgumentsException/IllegalConnectorArgumentsException
date: 2021-01-04
key: JavaJava.I.IllegalConnectorArgumentsException
category: java
tags: ['java se', 'com.sun.jdi.connect', 'jdk.jdi', 'metodo java', 'Java 1.3']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.I.IllegalConnectorArgumentsException.constructores valor="IllegalConnectorArgumentsException" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public IllegalConnectorArgumentsException(String s, String name)
public IllegalConnectorArgumentsException(String s, List<String> names)
~~~

## Parámetros
* **List&lt;String&gt; names**,  {% include w3api/param_description.html metodo=_data parametro="List<String> names" %}
* **String name**,  {% include w3api/param_description.html metodo=_data parametro="String name" %}
* **String s**,  {% include w3api/param_description.html metodo=_data parametro="String s" %}

## Clase Padre
[IllegalConnectorArgumentsException](/Java/IllegalConnectorArgumentsException/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.I.IllegalConnectorArgumentsException.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
