---
title: LoginModule.initialize()
permalink: /Java/LoginModule/initialize/
date: 2021-01-11
key: Java.L.LoginModule
category: Java
tags: ['java se', 'javax.security.auth.spi', 'java.base', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.L.LoginModule.metodos valor="initialize" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void initialize(Subject subject, CallbackHandler callbackHandler, Map<String,?> sharedState, Map<String,?> options)
~~~

## Parámetros
* **CallbackHandler callbackHandler**,  {% include w3api/param_description.html metodo=_dato parametro="CallbackHandler callbackHandler" %}
* **?&gt; sharedState**,  {% include w3api/param_description.html metodo=_dato parametro="?> sharedState" %}
* **Subject subject**,  {% include w3api/param_description.html metodo=_dato parametro="Subject subject" %}
* **Map&lt;String**,  {% include w3api/param_description.html metodo=_dato parametro="Map<String" %}
* **?&gt; options**,  {% include w3api/param_description.html metodo=_dato parametro="?> options" %}

## Clase Padre
[LoginModule](/Java/LoginModule/)

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
