---
title: ActivationSystem.activeGroup()
permalink: /Java/ActivationSystem/activeGroup/
date: 2021-01-11
key: Java.A.ActivationSystem
category: Java
tags: ['java se', 'java.rmi.activation', 'java.rmi', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.ActivationSystem.metodos valor="activeGroup" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
ActivationMonitor activeGroup(ActivationGroupID id, ActivationInstantiator group, long incarnation) throws UnknownGroupException, ActivationException, RemoteException
~~~

## Parámetros
* **long incarnation**,  {% include w3api/param_description.html metodo=_dato parametro="long incarnation" %}
* **ActivationInstantiator group**,  {% include w3api/param_description.html metodo=_dato parametro="ActivationInstantiator group" %}
* **ActivationGroupID id**,  {% include w3api/param_description.html metodo=_dato parametro="ActivationGroupID id" %}

## Excepciones
[ActivationException](/Java/ActivationException/), [UnknownGroupException](/Java/UnknownGroupException/), [RemoteException](/Java/RemoteException/)

## Clase Padre
[ActivationSystem](/Java/ActivationSystem/)

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
