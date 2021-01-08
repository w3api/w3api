---
title: KeyManagerFactorySpi.engineInit()
permalink: Java/KeyManagerFactorySpi/engineInit
date: 2021-01-04
key: JavaJava.K.KeyManagerFactorySpi
category: java
tags: ['java se', 'javax.net.ssl', 'java.base', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.K.KeyManagerFactorySpi.metodos valor="engineInit" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
protected abstract void engineInit(KeyStore ks, char[] password) throws KeyStoreException, NoSuchAlgorithmException, UnrecoverableKeyException
protected abstract void engineInit(ManagerFactoryParameters spec) throws InvalidAlgorithmParameterException
~~~

## Parámetros
* **ManagerFactoryParameters spec**,  {% include w3api/param_description.html metodo=_data parametro="ManagerFactoryParameters spec" %}
* **KeyStore ks**,  {% include w3api/param_description.html metodo=_data parametro="KeyStore ks" %}
* **char[] password**,  {% include w3api/param_description.html metodo=_data parametro="char[] password" %}

## Excepciones
[KeyStoreException](/Java/KeyStoreException/), [NoSuchAlgorithmException](/Java/NoSuchAlgorithmException/), [UnrecoverableKeyException](/Java/UnrecoverableKeyException/), [InvalidAlgorithmParameterException](/Java/InvalidAlgorithmParameterException/)

## Clase Padre
[KeyManagerFactorySpi](/Java/KeyManagerFactorySpi/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.K.KeyManagerFactorySpi.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
