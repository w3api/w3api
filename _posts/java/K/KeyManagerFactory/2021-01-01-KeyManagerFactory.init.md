---
title: KeyManagerFactory.init()
permalink: Java/KeyManagerFactory/init
date: 2021-01-11
key: JavaJava.K.KeyManagerFactory
category: java
tags: ['java se', 'javax.net.ssl', 'java.base', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.K.KeyManagerFactory.metodos valor="init" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public final void init(KeyStore ks, char[] password) throws KeyStoreException, NoSuchAlgorithmException, UnrecoverableKeyException
public final void init(ManagerFactoryParameters spec) throws InvalidAlgorithmParameterException
~~~

## Parámetros
* **ManagerFactoryParameters spec**,  {% include w3api/param_description.html metodo=_dato parametro="ManagerFactoryParameters spec" %}
* **char[] password**,  {% include w3api/param_description.html metodo=_dato parametro="char[] password" %}
* **KeyStore ks**,  {% include w3api/param_description.html metodo=_dato parametro="KeyStore ks" %}

## Excepciones
[NoSuchAlgorithmException](/Java/NoSuchAlgorithmException/), [InvalidAlgorithmParameterException](/Java/InvalidAlgorithmParameterException/), [UnrecoverableKeyException](/Java/UnrecoverableKeyException/), [KeyStoreException](/Java/KeyStoreException/)

## Clase Padre
[KeyManagerFactory](/Java/KeyManagerFactory/)

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
