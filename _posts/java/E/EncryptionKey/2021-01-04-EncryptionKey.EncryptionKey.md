---
title: EncryptionKey.EncryptionKey()
permalink: Java/EncryptionKey/EncryptionKey
date: 2021-01-04
key: JavaJava.E.EncryptionKey
category: java
tags: ['java se', 'javax.security.auth.kerberos', 'java.security.jgss', 'metodo java', 'Java 9']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.E.EncryptionKey.constructores valor="EncryptionKey" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public EncryptionKey(byte[] keyBytes, int keyType)
~~~

## Parámetros
* **byte[] keyBytes**,  {% include w3api/param_description.html metodo=_data parametro="byte[] keyBytes" %}
* **int keyType**,  {% include w3api/param_description.html metodo=_data parametro="int keyType" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/)

## Clase Padre
[EncryptionKey](/Java/EncryptionKey/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.E.EncryptionKey.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
