---
title: CertPathBuilder.getInstance()
permalink: Java/CertPathBuilder/getInstance
date: 2021-01-04
key: JavaJava.C.CertPathBuilder
category: java
tags: ['java se', 'java.security.cert', 'java.base', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.CertPathBuilder.metodos valor="getInstance" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static CertPathBuilder getInstance(String algorithm) throws NoSuchAlgorithmException
public static CertPathBuilder getInstance(String algorithm, String provider) throws NoSuchAlgorithmException, NoSuchProviderException
public static CertPathBuilder getInstance(String algorithm, Provider provider) throws NoSuchAlgorithmException
~~~

## Parámetros
* **String algorithm**,  {% include w3api/param_description.html metodo=_data parametro="String algorithm" %}
* **String provider**,  {% include w3api/param_description.html metodo=_data parametro="String provider" %}
* **Provider provider**,  {% include w3api/param_description.html metodo=_data parametro="Provider provider" %}

## Excepciones
[NoSuchAlgorithmException](/Java/NoSuchAlgorithmException/), [NullPointerException](/Java/NullPointerException/), [NoSuchProviderException](/Java/NoSuchProviderException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[CertPathBuilder](/Java/CertPathBuilder/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.C.CertPathBuilder.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
