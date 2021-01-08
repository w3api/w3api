---
title: KerberosKey.KerberosKey()
permalink: Java/KerberosKey/KerberosKey
date: 2021-01-04
key: JavaJava.K.KerberosKey
category: java
tags: ['java se', 'javax.security.auth.kerberos', 'java.security.jgss', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.K.KerberosKey.constructores valor="KerberosKey" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public KerberosKey(KerberosPrincipal principal, byte[] keyBytes, int keyType, int versionNum)
public KerberosKey(KerberosPrincipal principal, char[] password, String algorithm)
~~~

## Parámetros
* **byte[] keyBytes**,  {% include w3api/param_description.html metodo=_data parametro="byte[] keyBytes" %}
* **char[] password**,  {% include w3api/param_description.html metodo=_data parametro="char[] password" %}
* **String algorithm**,  {% include w3api/param_description.html metodo=_data parametro="String algorithm" %}
* **int keyType**,  {% include w3api/param_description.html metodo=_data parametro="int keyType" %}
* **int versionNum**,  {% include w3api/param_description.html metodo=_data parametro="int versionNum" %}
* **KerberosPrincipal principal**,  {% include w3api/param_description.html metodo=_data parametro="KerberosPrincipal principal" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[KerberosKey](/Java/KerberosKey/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.K.KerberosKey.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
