---
title: SecureRandom.getInstance()
permalink: /Java/SecureRandom/getInstance/
date: 2021-01-11
key: Java.S.SecureRandom
category: Java
tags: ['java se', 'java.security', 'java.base', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SecureRandom.metodos valor="getInstance" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static SecureRandom getInstance(String algorithm) throws NoSuchAlgorithmException
public static SecureRandom getInstance(String algorithm, String provider) throws NoSuchAlgorithmException, NoSuchProviderException
public static SecureRandom getInstance(String algorithm, Provider provider) throws NoSuchAlgorithmException
public static SecureRandom getInstance(String algorithm, SecureRandomParameters params) throws NoSuchAlgorithmException
public static SecureRandom getInstance(String algorithm, SecureRandomParameters params, String provider) throws NoSuchAlgorithmException, NoSuchProviderException
public static SecureRandom getInstance(String algorithm, SecureRandomParameters params, Provider provider) throws NoSuchAlgorithmException
~~~

## Parámetros
* **String algorithm**,  {% include w3api/param_description.html metodo=_dato parametro="String algorithm" %}
* **SecureRandomParameters params**,  {% include w3api/param_description.html metodo=_dato parametro="SecureRandomParameters params" %}
* **String provider**,  {% include w3api/param_description.html metodo=_dato parametro="String provider" %}
* **Provider provider**,  {% include w3api/param_description.html metodo=_dato parametro="Provider provider" %}

## Excepciones
[NoSuchAlgorithmException](/Java/NoSuchAlgorithmException/), [IllegalArgumentException](/Java/IllegalArgumentException/), [NoSuchProviderException](/Java/NoSuchProviderException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[SecureRandom](/Java/SecureRandom/)

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
