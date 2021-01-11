---
title: Krb5LoginModule.initialize()
permalink: Java/Krb5LoginModule/initialize
date: 2021-01-11
key: JavaJava.K.Krb5LoginModule
category: java
tags: ['java se', 'com.sun.security.auth.module', 'jdk.security.auth', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.K.Krb5LoginModule.metodos valor="initialize" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void initialize(Subject subject, CallbackHandler callbackHandler, Map<String,?> sharedState, Map<String,?> options)
~~~

## Parámetros
* **CallbackHandler callbackHandler**,  {% include w3api/param_description.html metodo=_dato parametro="CallbackHandler callbackHandler" %}
* **?&gt; sharedState**,  {% include w3api/param_description.html metodo=_dato parametro="?> sharedState" %}
* **Subject subject**,  {% include w3api/param_description.html metodo=_dato parametro="Subject subject" %}
* **Map&lt;String**,  {% include w3api/param_description.html metodo=_dato parametro="Map<String" %}
* **?&gt; options**,  {% include w3api/param_description.html metodo=_dato parametro="?> options" %}

## Clase Padre
[Krb5LoginModule](/Java/Krb5LoginModule/)

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
