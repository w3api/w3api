---
title: EncryptedPrivateKeyInfo.EncryptedPrivateKeyInfo()
permalink: Java/EncryptedPrivateKeyInfo/EncryptedPrivateKeyInfo
date: 2021-01-04
key: JavaJava.E.EncryptedPrivateKeyInfo
category: java
tags: ['java se', 'javax.crypto', 'java.base', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.E.EncryptedPrivateKeyInfo.constructores valor="EncryptedPrivateKeyInfo" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public EncryptedPrivateKeyInfo(byte[] encoded) throws IOException
public EncryptedPrivateKeyInfo(String algName, byte[] encryptedData) throws NoSuchAlgorithmException
public EncryptedPrivateKeyInfo(AlgorithmParameters algParams, byte[] encryptedData) throws NoSuchAlgorithmException
~~~

## Parámetros
* **byte[] encoded**,  {% include w3api/param_description.html metodo=_data parametro="byte[] encoded" %}
* **String algName**,  {% include w3api/param_description.html metodo=_data parametro="String algName" %}
* **byte[] encryptedData**,  {% include w3api/param_description.html metodo=_data parametro="byte[] encryptedData" %}
* **AlgorithmParameters algParams**,  {% include w3api/param_description.html metodo=_data parametro="AlgorithmParameters algParams" %}

## Excepciones
[NoSuchAlgorithmException](/Java/NoSuchAlgorithmException/), [IllegalArgumentException](/Java/IllegalArgumentException/), [NullPointerException](/Java/NullPointerException/), [IOException](/Java/IOException/)

## Clase Padre
[EncryptedPrivateKeyInfo](/Java/EncryptedPrivateKeyInfo/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.E.EncryptedPrivateKeyInfo.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
