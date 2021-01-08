---
title: JarSigner.Builder.JarSigner.Builder()
permalink: Java/JarSigner/Builder/JarSigner/Builder
date: 2021-01-04
key: JavaJava.J.JarSigner.Builder
category: java
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
* **PrivateKey privateKey**,  {% include w3api/param_description.html metodo=_data parametro="PrivateKey privateKey" %}
* **CertPath certPath**,  {% include w3api/param_description.html metodo=_data parametro="CertPath certPath" %}
* **KeyStore.PrivateKeyEntry entry**,  {% include w3api/param_description.html metodo=_data parametro="KeyStore.PrivateKeyEntry entry" %}

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
{%- for _ldc in site.data.Java.J.JarSigner.Builder.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
