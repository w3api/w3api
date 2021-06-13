---
title: JarSigner.sign()
permalink: /Java/JarSigner/sign/
date: 2021-01-11
key: Java.J.JarSigner
category: Java
tags: ['java se', 'jdk.security.jarsigner', 'jdk.jartool', 'metodo java', 'Java 9']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.J.JarSigner.metodos valor="sign" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void sign(ZipFile file, OutputStream os)
~~~

## Parámetros
* **OutputStream os**,  {% include w3api/param_description.html metodo=_dato parametro="OutputStream os" %}
* **ZipFile file**,  {% include w3api/param_description.html metodo=_dato parametro="ZipFile file" %}

## Excepciones
[JarSignerException](/Java/JarSignerException/)

## Clase Padre
[JarSigner](/Java/JarSigner/)

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
