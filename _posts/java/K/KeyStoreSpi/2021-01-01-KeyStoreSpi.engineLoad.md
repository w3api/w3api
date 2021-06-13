---
title: KeyStoreSpi.engineLoad()
permalink: /Java/KeyStoreSpi/engineLoad/
date: 2021-01-11
key: Java.K.KeyStoreSpi
category: Java
tags: ['java se', 'java.security', 'java.base', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.K.KeyStoreSpi.metodos valor="engineLoad" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract void engineLoad(InputStream stream, char[] password) throws IOException, NoSuchAlgorithmException, CertificateException
public void engineLoad(KeyStore.LoadStoreParameter param) throws IOException, NoSuchAlgorithmException, CertificateException
~~~

## Parámetros
* **char[] password**,  {% include w3api/param_description.html metodo=_dato parametro="char[] password" %}
* **InputStream stream**,  {% include w3api/param_description.html metodo=_dato parametro="InputStream stream" %}
* **KeyStore.LoadStoreParameter param**,  {% include w3api/param_description.html metodo=_dato parametro="KeyStore.LoadStoreParameter param" %}

## Excepciones
[NoSuchAlgorithmException](/Java/NoSuchAlgorithmException/), [CertificateException](/Java/CertificateException/), [IllegalArgumentException](/Java/IllegalArgumentException/), [IOException](/Java/IOException/)

## Clase Padre
[KeyStoreSpi](/Java/KeyStoreSpi/)

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
