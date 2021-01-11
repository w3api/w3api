---
title: ContentSigner.generateSignedData()
permalink: Java/ContentSigner/generateSignedData
date: 2021-01-11
key: JavaJava.C.ContentSigner
category: java
tags: ['java se', 'com.sun.jarsigner', 'jdk.jartool', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.ContentSigner.metodos valor="generateSignedData" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract byte[] generateSignedData(ContentSignerParameters parameters, boolean omitContent, boolean applyTimestamp) throws NoSuchAlgorithmException, CertificateException, IOException
~~~

## Parámetros
* **boolean applyTimestamp**,  {% include w3api/param_description.html metodo=_dato parametro="boolean applyTimestamp" %}
* **ContentSignerParameters parameters**,  {% include w3api/param_description.html metodo=_dato parametro="ContentSignerParameters parameters" %}
* **boolean omitContent**,  {% include w3api/param_description.html metodo=_dato parametro="boolean omitContent" %}

## Excepciones
[NoSuchAlgorithmException](/Java/NoSuchAlgorithmException/), [CertificateException](/Java/CertificateException/), [NullPointerException](/Java/NullPointerException/), [IOException](/Java/IOException/)

## Clase Padre
[ContentSigner](/Java/ContentSigner/)

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
