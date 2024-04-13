---
title: JarSigner.Builder.JarSigner.Builder()
permalink: /Java/JarSigner/Builder/JarSigner/Builder/
date: 2021-01-11
key: Java.J.JarSigner.Builder
category: Java
tags: ['java se', 'jdk.security.jarsigner', 'jdk.jartool', 'metodo java', 'Java 9']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.J.JarSigner.Builder.constructores valor="JarSigner.Builder" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public Builder(KeyStore.PrivateKeyEntry entry)
public Builder(PrivateKey privateKey, CertPath certPath)
~~~

## Parámetros
* **CertPath certPath**,  {% include w3api/param_description.html metodo=_dato parametro="CertPath certPath" %}
* **KeyStore.PrivateKeyEntry entry**,  {% include w3api/param_description.html metodo=_dato parametro="KeyStore.PrivateKeyEntry entry" %}
* **PrivateKey privateKey**,  {% include w3api/param_description.html metodo=_dato parametro="PrivateKey privateKey" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[JarSigner.Builder](/Java/JarSigner/Builder/)

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
