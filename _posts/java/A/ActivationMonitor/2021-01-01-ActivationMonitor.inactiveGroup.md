---
title: ActivationMonitor.inactiveGroup()
permalink: Java/ActivationMonitor/inactiveGroup
date: 2021-01-11
key: JavaJava.A.ActivationMonitor
category: java
tags: ['java se', 'java.rmi.activation', 'java.rmi', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.ActivationMonitor.metodos valor="inactiveGroup" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void inactiveGroup(ActivationGroupID id, long incarnation) throws UnknownGroupException, RemoteException
~~~

## Parámetros
* **long incarnation**,  {% include w3api/param_description.html metodo=_dato parametro="long incarnation" %}
* **ActivationGroupID id**,  {% include w3api/param_description.html metodo=_dato parametro="ActivationGroupID id" %}

## Excepciones
[UnknownGroupException](/Java/UnknownGroupException/), [RemoteException](/Java/RemoteException/)

## Clase Padre
[ActivationMonitor](/Java/ActivationMonitor/)

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
