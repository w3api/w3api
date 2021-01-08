---
title: JndiLoginModule.initialize()
permalink: Java/JndiLoginModule/initialize
date: 2021-01-04
key: JavaJava.J.JndiLoginModule
category: java
tags: ['java se', 'com.sun.security.auth.module', 'jdk.security.auth', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.J.JndiLoginModule.metodos valor="initialize" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void initialize(Subject subject, CallbackHandler callbackHandler, Map<String,?> sharedState, Map<String,?> options)
~~~

## Parámetros
* **Subject subject**,  {% include w3api/param_description.html metodo=_data parametro="Subject subject" %}
* **?&gt; options**,  {% include w3api/param_description.html metodo=_data parametro="?> options" %}
* **Map&lt;String**,  {% include w3api/param_description.html metodo=_data parametro="Map<String" %}
* **CallbackHandler callbackHandler**,  {% include w3api/param_description.html metodo=_data parametro="CallbackHandler callbackHandler" %}
* **?&gt; sharedState**,  {% include w3api/param_description.html metodo=_data parametro="?> sharedState" %}

## Clase Padre
[JndiLoginModule](/Java/JndiLoginModule/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.J.JndiLoginModule.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
