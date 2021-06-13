---
title: KerberosTicket.refresh()
permalink: /Java/KerberosTicket/refresh/
date: 2021-01-11
key: Java.K.KerberosTicket
category: Java
tags: ['java se', 'javax.security.auth.kerberos', 'java.security.jgss', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.K.KerberosTicket.metodos valor="refresh" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void refresh() throws RefreshFailedException
~~~

## Excepciones
[RefreshFailedException](/Java/RefreshFailedException/), [IllegalStateException](/Java/IllegalStateException/)

## Clase Padre
[KerberosTicket](/Java/KerberosTicket/)

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
