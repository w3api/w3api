---
title: TransformService.getInstance()
permalink: Java/TransformService/getInstance
date: 2021-01-11
key: JavaJava.T.TransformService
category: java
tags: ['java se', 'javax.xml.crypto.dsig', 'java.xml.crypto', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.T.TransformService.metodos valor="getInstance" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static TransformService getInstance(String algorithm, String mechanismType) throws NoSuchAlgorithmException
public static TransformService getInstance(String algorithm, String mechanismType, String provider) throws NoSuchAlgorithmException, NoSuchProviderException
public static TransformService getInstance(String algorithm, String mechanismType, Provider provider) throws NoSuchAlgorithmException
~~~

## Parámetros
* **String algorithm**,  {% include w3api/param_description.html metodo=_dato parametro="String algorithm" %}
* **String provider**,  {% include w3api/param_description.html metodo=_dato parametro="String provider" %}
* **String mechanismType**,  {% include w3api/param_description.html metodo=_dato parametro="String mechanismType" %}
* **Provider provider**,  {% include w3api/param_description.html metodo=_dato parametro="Provider provider" %}

## Excepciones
[NoSuchAlgorithmException](/Java/NoSuchAlgorithmException/), [NoSuchProviderException](/Java/NoSuchProviderException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[TransformService](/Java/TransformService/)

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
