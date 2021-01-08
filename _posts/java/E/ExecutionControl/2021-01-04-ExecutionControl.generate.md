---
title: ExecutionControl.generate()
permalink: Java/ExecutionControl/generate
date: 2021-01-04
key: JavaJava.E.ExecutionControl
category: java
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
* **String&gt; parameters**,  {% include w3api/param_description.html metodo=_data parametro="String> parameters" %}
* **ExecutionEnv env**,  {% include w3api/param_description.html metodo=_data parametro="ExecutionEnv env" %}
* **Map&lt;String**,  {% include w3api/param_description.html metodo=_data parametro="Map<String" %}
* **String spec**,  {% include w3api/param_description.html metodo=_data parametro="String spec" %}
* **String name**,  {% include w3api/param_description.html metodo=_data parametro="String name" %}

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
{%- for _ldc in site.data.Java.E.ExecutionControl.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
