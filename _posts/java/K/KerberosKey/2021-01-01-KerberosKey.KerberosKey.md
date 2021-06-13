---
title: KerberosKey.KerberosKey()
permalink: /Java/KerberosKey/KerberosKey/
date: 2021-01-11
key: Java.K.KerberosKey
category: Java
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
* **byte[] keyBytes**,  {% include w3api/param_description.html metodo=_dato parametro="byte[] keyBytes" %}
* **KerberosPrincipal principal**,  {% include w3api/param_description.html metodo=_dato parametro="KerberosPrincipal principal" %}
* **int versionNum**,  {% include w3api/param_description.html metodo=_dato parametro="int versionNum" %}
* **char[] password**,  {% include w3api/param_description.html metodo=_dato parametro="char[] password" %}
* **String algorithm**,  {% include w3api/param_description.html metodo=_dato parametro="String algorithm" %}
* **int keyType**,  {% include w3api/param_description.html metodo=_dato parametro="int keyType" %}

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
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
