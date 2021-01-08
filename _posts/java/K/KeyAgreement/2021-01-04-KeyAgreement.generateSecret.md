---
title: KeyAgreement.generateSecret()
permalink: Java/KeyAgreement/generateSecret
date: 2021-01-04
key: JavaJava.K.KeyAgreement
category: java
tags: ['java se', 'javax.crypto', 'java.base', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.K.KeyAgreement.metodos valor="generateSecret" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public final byte[] generateSecret() throws IllegalStateException
public final int generateSecret(byte[] sharedSecret, int offset) throws IllegalStateException, ShortBufferException
public final SecretKey generateSecret(String algorithm) throws IllegalStateException, NoSuchAlgorithmException, InvalidKeyException
~~~

## Parámetros
* **String algorithm**,  {% include w3api/param_description.html metodo=_data parametro="String algorithm" %}
* **byte[] sharedSecret**,  {% include w3api/param_description.html metodo=_data parametro="byte[] sharedSecret" %}
* **int offset**,  {% include w3api/param_description.html metodo=_data parametro="int offset" %}

## Excepciones
[ShortBufferException](/Java/ShortBufferException/), [IllegalStateException](/Java/IllegalStateException/), [InvalidKeyException](/Java/InvalidKeyException/), [NoSuchAlgorithmException](/Java/NoSuchAlgorithmException/)

## Clase Padre
[KeyAgreement](/Java/KeyAgreement/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.K.KeyAgreement.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
