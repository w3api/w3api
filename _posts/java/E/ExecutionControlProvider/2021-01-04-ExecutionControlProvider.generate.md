---
title: ExecutionControlProvider.generate()
permalink: Java/ExecutionControlProvider/generate
date: 2021-01-04
key: JavaJava.E.ExecutionControlProvider
category: java
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
* **String&gt; parameters**,  {% include w3api/param_description.html metodo=_data parametro="String> parameters" %}
* **ExecutionEnv env**,  {% include w3api/param_description.html metodo=_data parametro="ExecutionEnv env" %}
* **Map&lt;String**,  {% include w3api/param_description.html metodo=_data parametro="Map<String" %}

## Clase Padre
[ExecutionControlProvider](/Java/ExecutionControlProvider/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.E.ExecutionControlProvider.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
