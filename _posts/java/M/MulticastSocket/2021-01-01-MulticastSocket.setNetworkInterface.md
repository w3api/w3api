---
title: MulticastSocket.setNetworkInterface()
permalink: Java/MulticastSocket/setNetworkInterface
date: 2021-01-11
key: JavaJava.M.MulticastSocket
category: java
tags: ['java se', 'java.net', 'java.base', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.M.MulticastSocket.metodos valor="setNetworkInterface" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void setNetworkInterface(NetworkInterface netIf) throws SocketException
~~~

## Parámetros
* **NetworkInterface netIf**,  {% include w3api/param_description.html metodo=_dato parametro="NetworkInterface netIf" %}

## Excepciones
[SocketException](/Java/SocketException/)

## Clase Padre
[MulticastSocket](/Java/MulticastSocket/)

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
