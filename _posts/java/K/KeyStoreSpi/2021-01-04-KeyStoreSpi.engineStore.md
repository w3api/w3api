---
title: KeyStoreSpi.engineStore()
permalink: Java/KeyStoreSpi/engineStore
date: 2021-01-04
key: JavaJava.K.KeyStoreSpi
category: java
tags: ['java se', 'java.security', 'java.base', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.K.KeyStoreSpi.metodos valor="engineStore" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract void engineStore(OutputStream stream, char[] password) throws IOException, NoSuchAlgorithmException, CertificateException
public void engineStore(KeyStore.LoadStoreParameter param) throws IOException, NoSuchAlgorithmException, CertificateException
~~~

## Parámetros
* **OutputStream stream**,  {% include w3api/param_description.html metodo=_data parametro="OutputStream stream" %}
* **KeyStore.LoadStoreParameter param**,  {% include w3api/param_description.html metodo=_data parametro="KeyStore.LoadStoreParameter param" %}
* **char[] password**,  {% include w3api/param_description.html metodo=_data parametro="char[] password" %}

## Excepciones
[NoSuchAlgorithmException](/Java/NoSuchAlgorithmException/), [IllegalArgumentException](/Java/IllegalArgumentException/), [CertificateException](/Java/CertificateException/), [IOException](/Java/IOException/)

## Clase Padre
[KeyStoreSpi](/Java/KeyStoreSpi/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.K.KeyStoreSpi.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
