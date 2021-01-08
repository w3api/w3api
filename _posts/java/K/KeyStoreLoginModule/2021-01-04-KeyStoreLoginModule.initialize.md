---
title: KeyStoreLoginModule.initialize()
permalink: Java/KeyStoreLoginModule/initialize
date: 2021-01-04
key: JavaJava.K.KeyStoreLoginModule
category: java
tags: ['java se', 'com.sun.security.auth.module', 'jdk.security.auth', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.K.KeyStoreLoginModule.metodos valor="initialize" %}

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
[KeyStoreLoginModule](/Java/KeyStoreLoginModule/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.K.KeyStoreLoginModule.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
