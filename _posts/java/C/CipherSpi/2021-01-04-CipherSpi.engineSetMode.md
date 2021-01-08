---
title: CipherSpi.engineSetMode()
permalink: Java/CipherSpi/engineSetMode
date: 2021-01-04
key: JavaJava.C.CipherSpi
category: java
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
* **String mode**,  {% include w3api/param_description.html metodo=_data parametro="String mode" %}

## Excepciones
[NoSuchAlgorithmException](/Java/NoSuchAlgorithmException/)

## Clase Padre
[CipherSpi](/Java/CipherSpi/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.C.CipherSpi.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
