---
title: SealedObject.getObject()
permalink: Java/SealedObject/getObject
date: 2021-01-04
key: JavaJava.S.SealedObject
category: java
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
* **String provider**,  {% include w3api/param_description.html metodo=_data parametro="String provider" %}
* **Key key**,  {% include w3api/param_description.html metodo=_data parametro="Key key" %}
* **Cipher c**,  {% include w3api/param_description.html metodo=_data parametro="Cipher c" %}

## Excepciones
[IllegalBlockSizeException](/Java/IllegalBlockSizeException/), [NoSuchAlgorithmException](/Java/NoSuchAlgorithmException/), [IllegalArgumentException](/Java/IllegalArgumentException/), [InvalidKeyException](/Java/InvalidKeyException/), [NullPointerException](/Java/NullPointerException/), [NoSuchProviderException](/Java/NoSuchProviderException/), [ClassNotFoundException](/Java/ClassNotFoundException/), [BadPaddingException](/Java/BadPaddingException/), [IOException](/Java/IOException/)

## Clase Padre
[SealedObject](/Java/SealedObject/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.S.SealedObject.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
