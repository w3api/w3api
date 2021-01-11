---
title: KeyManagerFactory.getInstance()
permalink: Java/KeyManagerFactory/getInstance
date: 2021-01-11
key: JavaJava.K.KeyManagerFactory
category: java
tags: ['java se', 'javax.net.ssl', 'java.base', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.K.KeyManagerFactory.metodos valor="getInstance" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
static KeyManagerFactory getInstance(String algorithm)
static KeyManagerFactory getInstance(String algorithm, String provider)
static KeyManagerFactory getInstance(String algorithm, Provider provider)
~~~

## Parámetros
* **String algorithm**,  {% include w3api/param_description.html metodo=_dato parametro="String algorithm" %}
* **String provider**,  {% include w3api/param_description.html metodo=_dato parametro="String provider" %}
* **Provider provider**,  {% include w3api/param_description.html metodo=_dato parametro="Provider provider" %}

## Clase Padre
[KeyManagerFactory](/Java/KeyManagerFactory/)

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
