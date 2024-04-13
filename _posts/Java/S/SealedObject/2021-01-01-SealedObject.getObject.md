---
title: SealedObject.getObject()
permalink: /Java/SealedObject/getObject/
date: 2021-01-11
key: Java.S.SealedObject
category: Java
tags: ['java se', 'javax.crypto', 'java.base', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SealedObject.metodos valor="getObject" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public final Object getObject(Key key) throws IOException, ClassNotFoundException, NoSuchAlgorithmException, InvalidKeyException
public final Object getObject(Key key, String provider) throws IOException, ClassNotFoundException, NoSuchAlgorithmException, NoSuchProviderException, InvalidKeyException
public final Object getObject(Cipher c) throws IOException, ClassNotFoundException, IllegalBlockSizeException, BadPaddingException
~~~

## Parámetros
* **Cipher c**,  {% include w3api/param_description.html metodo=_dato parametro="Cipher c" %}
* **String provider**,  {% include w3api/param_description.html metodo=_dato parametro="String provider" %}
* **Key key**,  {% include w3api/param_description.html metodo=_dato parametro="Key key" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/), [NoSuchProviderException](/Java/NoSuchProviderException/), [IOException](/Java/IOException/), [BadPaddingException](/Java/BadPaddingException/), [IllegalBlockSizeException](/Java/IllegalBlockSizeException/), [NoSuchAlgorithmException](/Java/NoSuchAlgorithmException/), [ClassNotFoundException](/Java/ClassNotFoundException/), [InvalidKeyException](/Java/InvalidKeyException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[SealedObject](/Java/SealedObject/)

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
