---
title: ExecutionControl.generate()
permalink: /Java/ExecutionControl/generate/
date: 2021-01-11
key: Java.E.ExecutionControl
category: Java
tags: ['java se', 'jdk.jshell.spi', 'jdk.jshell', 'metodo java', 'Java 9']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.E.ExecutionControl.metodos valor="generate" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
static ExecutionControl generate(ExecutionEnv env, String spec) throws Throwable
static ExecutionControl generate(ExecutionEnv env, String name, Map<String,String> parameters) throws Throwable
~~~

## Parámetros
* **String name**,  {% include w3api/param_description.html metodo=_dato parametro="String name" %}
* **String spec**,  {% include w3api/param_description.html metodo=_dato parametro="String spec" %}
* **ExecutionEnv env**,  {% include w3api/param_description.html metodo=_dato parametro="ExecutionEnv env" %}
* **String&gt; parameters**,  {% include w3api/param_description.html metodo=_dato parametro="String> parameters" %}
* **Map&lt;String**,  {% include w3api/param_description.html metodo=_dato parametro="Map<String" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[ExecutionControl](/Java/ExecutionControl/)

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
