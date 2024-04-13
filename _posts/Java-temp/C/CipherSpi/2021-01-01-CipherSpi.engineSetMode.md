---
title: CipherSpi.engineSetMode()
permalink: /Java/CipherSpi/engineSetMode/
date: 2021-01-11
key: Java.C.CipherSpi
category: Java
tags: ['java se', 'javax.crypto', 'java.base', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.CipherSpi.metodos valor="engineSetMode" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
protected abstract void engineSetMode(String mode) throws NoSuchAlgorithmException
~~~

## Parámetros
* **String mode**,  {% include w3api/param_description.html metodo=_dato parametro="String mode" %}

## Excepciones
[NoSuchAlgorithmException](/Java/NoSuchAlgorithmException/)

## Clase Padre
[CipherSpi](/Java/CipherSpi/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Artículos
<ul>
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
