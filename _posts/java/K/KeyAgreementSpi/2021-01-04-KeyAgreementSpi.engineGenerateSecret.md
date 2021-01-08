---
title: KeyAgreementSpi.engineGenerateSecret()
permalink: Java/KeyAgreementSpi/engineGenerateSecret
date: 2021-01-04
key: JavaJava.K.KeyAgreementSpi
category: java
tags: ['java se', 'javax.crypto', 'java.base', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.K.KeyAgreementSpi.metodos valor="engineGenerateSecret" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
protected abstract byte[] engineGenerateSecret() throws IllegalStateException
protected abstract int engineGenerateSecret(byte[] sharedSecret, int offset) throws IllegalStateException, ShortBufferException
protected abstract SecretKey engineGenerateSecret(String algorithm) throws IllegalStateException, NoSuchAlgorithmException, InvalidKeyException
~~~

## Parámetros
* **String algorithm**,  {% include w3api/param_description.html metodo=_data parametro="String algorithm" %}
* **byte[] sharedSecret**,  {% include w3api/param_description.html metodo=_data parametro="byte[] sharedSecret" %}
* **int offset**,  {% include w3api/param_description.html metodo=_data parametro="int offset" %}

## Excepciones
[ShortBufferException](/Java/ShortBufferException/), [IllegalStateException](/Java/IllegalStateException/), [InvalidKeyException](/Java/InvalidKeyException/), [NoSuchAlgorithmException](/Java/NoSuchAlgorithmException/)

## Clase Padre
[KeyAgreementSpi](/Java/KeyAgreementSpi/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.K.KeyAgreementSpi.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
