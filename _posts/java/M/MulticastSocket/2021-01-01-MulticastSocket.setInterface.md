---
title: MulticastSocket.setInterface()
permalink: /Java/MulticastSocket/setInterface/
date: 2021-01-11
key: Java.M.MulticastSocket
category: Java
tags: ['java se', 'java.net', 'java.base', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.M.MulticastSocket.metodos valor="setInterface" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void setInterface(InetAddress inf) throws SocketException
~~~

## Parámetros
* **InetAddress inf**,  {% include w3api/param_description.html metodo=_dato parametro="InetAddress inf" %}

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
