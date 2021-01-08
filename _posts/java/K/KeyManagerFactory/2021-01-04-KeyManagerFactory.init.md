---
title: KeyManagerFactory.init()
permalink: Java/KeyManagerFactory/init
date: 2021-01-04
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
* **ManagerFactoryParameters spec**,  {% include w3api/param_description.html metodo=_data parametro="ManagerFactoryParameters spec" %}
* **KeyStore ks**,  {% include w3api/param_description.html metodo=_data parametro="KeyStore ks" %}
* **char[] password**,  {% include w3api/param_description.html metodo=_data parametro="char[] password" %}

## Excepciones
[KeyStoreException](/Java/KeyStoreException/), [NoSuchAlgorithmException](/Java/NoSuchAlgorithmException/), [UnrecoverableKeyException](/Java/UnrecoverableKeyException/), [InvalidAlgorithmParameterException](/Java/InvalidAlgorithmParameterException/)

## Clase Padre
[KeyManagerFactory](/Java/KeyManagerFactory/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.K.KeyManagerFactory.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
