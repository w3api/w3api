---
title: SecretKeyFactory.getInstance()
permalink: /Java/SecretKeyFactory/getInstance/
date: 2021-01-11
key: Java.S.SecretKeyFactory
category: Java
tags: ['java se', 'javax.crypto', 'java.base', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SecretKeyFactory.metodos valor="getInstance" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
static SecretKeyFactory getInstance(String algorithm)
static SecretKeyFactory getInstance(String algorithm, String provider)
static SecretKeyFactory getInstance(String algorithm, Provider provider)
~~~

## Parámetros
* **String algorithm**,  {% include w3api/param_description.html metodo=_dato parametro="String algorithm" %}
* **String provider**,  {% include w3api/param_description.html metodo=_dato parametro="String provider" %}
* **Provider provider**,  {% include w3api/param_description.html metodo=_dato parametro="Provider provider" %}

## Clase Padre
[SecretKeyFactory](/Java/SecretKeyFactory/)

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
