---
title: ExecutionControlProvider.generate()
permalink: /Java/ExecutionControlProvider/generate/
date: 2021-01-11
key: Java.E.ExecutionControlProvider
category: Java
tags: ['java se', 'jdk.jshell.spi', 'jdk.jshell', 'metodo java', 'Java 9']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.E.ExecutionControlProvider.metodos valor="generate" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
ExecutionControl generate(ExecutionEnv env, Map<String,String> parameters) throws Throwable
~~~

## Parámetros
* **ExecutionEnv env**,  {% include w3api/param_description.html metodo=_dato parametro="ExecutionEnv env" %}
* **Map&lt;String**,  {% include w3api/param_description.html metodo=_dato parametro="Map<String" %}
* **String&gt; parameters**,  {% include w3api/param_description.html metodo=_dato parametro="String> parameters" %}

## Clase Padre
[ExecutionControlProvider](/Java/ExecutionControlProvider/)

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
