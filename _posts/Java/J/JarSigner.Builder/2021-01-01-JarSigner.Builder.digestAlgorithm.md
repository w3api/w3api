---
title: JarSigner.Builder.digestAlgorithm()
permalink: /Java/JarSigner/Builder/digestAlgorithm/
date: 2021-01-11
key: Java.J.JarSigner.Builder
category: Java
tags: ['java se', 'jdk.security.jarsigner', 'jdk.jartool', 'metodo java', 'Java 9']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.J.JarSigner.Builder.metodos valor="digestAlgorithm" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public JarSigner.Builder digestAlgorithm(String algorithm) throws NoSuchAlgorithmException
public JarSigner.Builder digestAlgorithm(String algorithm, Provider provider) throws NoSuchAlgorithmException
~~~

## Parámetros
* **String algorithm**,  {% include w3api/param_description.html metodo=_dato parametro="String algorithm" %}
* **Provider provider**,  {% include w3api/param_description.html metodo=_dato parametro="Provider provider" %}

## Excepciones
[NoSuchAlgorithmException](/Java/NoSuchAlgorithmException/)

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
