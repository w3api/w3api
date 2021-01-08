---
title: KerberosCredMessage.KerberosCredMessage()
permalink: Java/KerberosCredMessage/KerberosCredMessage
date: 2021-01-04
key: JavaJava.K.KerberosCredMessage
category: java
tags: ['java se', 'javax.security.auth.kerberos', 'java.security.jgss', 'metodo java', 'Java 9']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.K.KerberosCredMessage.constructores valor="KerberosCredMessage" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public KerberosCredMessage(KerberosPrincipal sender, KerberosPrincipal recipient, byte[] message)
~~~

## Parámetros
* **KerberosPrincipal sender**,  {% include w3api/param_description.html metodo=_data parametro="KerberosPrincipal sender" %}
* **byte[] message**,  {% include w3api/param_description.html metodo=_data parametro="byte[] message" %}
* **KerberosPrincipal recipient**,  {% include w3api/param_description.html metodo=_data parametro="KerberosPrincipal recipient" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/)

## Clase Padre
[KerberosCredMessage](/Java/KerberosCredMessage/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.K.KerberosCredMessage.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
