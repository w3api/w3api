---
title: SSLServerSocket.setEnabledProtocols()
permalink: Java/SSLServerSocket/setEnabledProtocols
date: 2021-01-04
key: JavaJava.S.SSLServerSocket
category: java
tags: ['java se', 'javax.net.ssl', 'java.base', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SSLServerSocket.metodos valor="setEnabledProtocols" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract void setEnabledProtocols(String[] protocols)
~~~

## Parámetros
* **String[] protocols**,  {% include w3api/param_description.html metodo=_data parametro="String[] protocols" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[SSLServerSocket](/Java/SSLServerSocket/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.S.SSLServerSocket.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
