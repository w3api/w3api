---
title: EncryptedPrivateKeyInfo.getKeySpec()
permalink: Java/EncryptedPrivateKeyInfo/getKeySpec
date: 2021-01-11
key: JavaJava.E.EncryptedPrivateKeyInfo
category: java
tags: ['java se', 'javax.crypto', 'java.base', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.E.EncryptedPrivateKeyInfo.metodos valor="getKeySpec" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public PKCS8EncodedKeySpec getKeySpec(Key decryptKey) throws NoSuchAlgorithmException, InvalidKeyException
public PKCS8EncodedKeySpec getKeySpec(Key decryptKey, String providerName) throws NoSuchProviderException, NoSuchAlgorithmException, InvalidKeyException
public PKCS8EncodedKeySpec getKeySpec(Key decryptKey, Provider provider) throws NoSuchAlgorithmException, InvalidKeyException
public PKCS8EncodedKeySpec getKeySpec(Cipher cipher) throws InvalidKeySpecException
~~~

## Parámetros
* **Provider provider**,  {% include w3api/param_description.html metodo=_dato parametro="Provider provider" %}
* **String providerName**,  {% include w3api/param_description.html metodo=_dato parametro="String providerName" %}
* **Key decryptKey**,  {% include w3api/param_description.html metodo=_dato parametro="Key decryptKey" %}
* **Cipher cipher**,  {% include w3api/param_description.html metodo=_dato parametro="Cipher cipher" %}

## Excepciones
[NoSuchProviderException](/Java/NoSuchProviderException/), [InvalidKeySpecException](/Java/InvalidKeySpecException/), [NoSuchAlgorithmException](/Java/NoSuchAlgorithmException/), [InvalidKeyException](/Java/InvalidKeyException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[EncryptedPrivateKeyInfo](/Java/EncryptedPrivateKeyInfo/)

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
